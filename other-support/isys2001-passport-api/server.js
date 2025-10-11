const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const sqlite3 = require('sqlite3').verbose();
const crypto = require('crypto');
const jwt = require('jsonwebtoken');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;
const JWT_SECRET = process.env.JWT_SECRET || 'your-secret-key-change-this';
const ADMIN_KEY = process.env.ADMIN_KEY || 'admin-secret-key';

// Middleware
app.use(helmet());
app.use(cors());
app.use(express.json());

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 10 // limit each IP to 10 requests per windowMs
});
app.use('/api/verify', limiter);

// Initialize SQLite database
const db = new sqlite3.Database('./passport.db');

db.run(`
  CREATE TABLE IF NOT EXISTS stamps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    week INTEGER NOT NULL,
    tool TEXT NOT NULL,
    stamp_code TEXT UNIQUE NOT NULL,
    workspace_url TEXT,
    secret_code TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    ip_address TEXT,
    verified BOOLEAN DEFAULT 1,
    UNIQUE(email, week)
  )
`);

db.run(`
  CREATE TABLE IF NOT EXISTS students (
    email TEXT PRIMARY KEY,
    name TEXT,
    student_id TEXT,
    total_stamps INTEGER DEFAULT 0,
    last_activity DATETIME DEFAULT CURRENT_TIMESTAMP
  )
`);

// Weekly configuration
const WEEKLY_CONFIG = {
  1: { tool: 'Lucidchart', secrets: ['FLOWCHART-MASTER-2025', 'LOGIC-FLOW-ROCKS', 'DIAGRAM-WIZARD'] },
  2: { tool: 'Scratch', secrets: ['SCRATCH-CAT-RULES', 'BLOCK-CODE-FUN', 'VISUAL-LOGIC-101'] },
  3: { tool: 'Orange', secrets: ['ORANGE-UNICORN-42', 'DATA-MINING-ROCKS', 'WORKFLOW-WIZARD'] },
  4: { tool: 'n8n', secrets: ['AUTOMATE-ALL-THINGS', 'WORKFLOW-NINJA', 'N8N-POWER-USER'] },
  5: { tool: 'AI-Tools', secrets: ['PROMPT-ENGINEER-PRO', 'AI-COLLABORATOR', 'DEBUG-THE-BOT'] },
  6: { tool: 'Sonic-Pi', secrets: ['MUSIC-CODE-BEATS', 'ALGORITHMIC-MELODY', 'SONIC-SYMPHONY'] },
  7: { tool: 'Twine', secrets: ['STORY-BRANCH-MASTER', 'INTERACTIVE-TALES', 'CHOOSE-ADVENTURE'] },
  8: { tool: 'Observable', secrets: ['DATA-VIZ-EXPERT', 'DASHBOARD-DYNAMO', 'REACTIVE-CHARTS'] },
  9: { tool: 'Pico-8', secrets: ['PIXEL-PERFECT-GAME', 'TINY-GAME-GIANT-FUN', 'CONSTRAINT-CREATIVE'] },
  10: { tool: 'Voiceflow', secrets: ['CHATBOT-CREATOR', 'CONVERSATION-DESIGN', 'VOICE-FIRST-DEV'] },
  11: { tool: 'App-Inventor', secrets: ['MOBILE-APP-MAKER', 'DRAG-DROP-DEPLOY', 'APP-WIZARD-2025'] },
  12: { tool: 'Integration', secrets: ['FULL-STACK-HERO', 'TOOLS-SYNTHESIZER', 'DIGITAL-ARCHITECT'] }
};

// Helper functions
function generateStampCode(email, week, secret) {
  const data = `${email}|${week}|${secret}|${JWT_SECRET}`;
  return 'ISYS2001-W' + week + '-' + crypto.createHash('sha256').update(data).digest('hex').substring(0, 8).toUpperCase();
}

// API Routes

// 1. Generate stamp
app.post('/api/generate-stamp', async (req, res) => {
  try {
    const { email, week, workspace_url, secret_code } = req.body;
    const ip_address = req.ip;

    // Validate inputs
    if (!email || !week || !workspace_url || !secret_code) {
      return res.status(400).json({ success: false, message: 'Missing required fields' });
    }

    // Validate week
    if (week < 1 || week > 12) {
      return res.status(400).json({ success: false, message: 'Invalid week number' });
    }

    // Validate secret code
    const weekConfig = WEEKLY_CONFIG[week];
    if (!weekConfig.secrets.includes(secret_code.toUpperCase())) {
      return res.status(400).json({ success: false, message: 'Invalid secret code' });
    }

    // Check if student already has stamp for this week
    db.get('SELECT * FROM stamps WHERE email = ? AND week = ?', [email, week], (err, existing) => {
      if (existing) {
        return res.json({ 
          success: true, 
          stamp_code: existing.stamp_code,
          message: 'You already have a stamp for this week!',
          existing: true 
        });
      }

      // Generate new stamp
      const stamp_code = generateStampCode(email, week, secret_code);
      const tool = weekConfig.tool;

      // Insert into database
      db.run(
        'INSERT INTO stamps (email, week, tool, stamp_code, workspace_url, secret_code, ip_address) VALUES (?, ?, ?, ?, ?, ?, ?)',
        [email, week, tool, stamp_code, workspace_url, secret_code, ip_address],
        function(err) {
          if (err) {
            return res.status(500).json({ success: false, message: 'Database error' });
          }

          // Update student record
          db.run(
            'INSERT OR REPLACE INTO students (email, total_stamps, last_activity) VALUES (?, COALESCE((SELECT total_stamps FROM students WHERE email = ?), 0) + 1, CURRENT_TIMESTAMP)',
            [email, email]
          );

          res.json({
            success: true,
            stamp_code: stamp_code,
            week: week,
            tool: tool,
            message: 'Stamp generated successfully!'
          });
        }
      );
    });
  } catch (error) {
    console.error('Error:', error);
    res.status(500).json({ success: false, message: 'Server error' });
  }
});

// 2. Verify stamp
app.post('/api/verify-stamp', (req, res) => {
  const { stamp_code, email } = req.body;

  db.get(
    'SELECT * FROM stamps WHERE stamp_code = ? AND email = ?',
    [stamp_code, email],
    (err, stamp) => {
      if (err || !stamp) {
        return res.json({ success: false, valid: false, message: 'Invalid stamp code' });
      }

      res.json({
        success: true,
        valid: true,
        week: stamp.week,
        tool: stamp.tool,
        timestamp: stamp.timestamp
      });
    }
  );
});

// 3. Get student progress
app.get('/api/progress/:email', (req, res) => {
  const email = req.params.email;

  db.all(
    'SELECT week, tool, stamp_code, timestamp FROM stamps WHERE email = ? ORDER BY week',
    [email],
    (err, stamps) => {
      if (err) {
        return res.status(500).json({ success: false, message: 'Database error' });
      }

      const progress = {
        email: email,
        total_stamps: stamps.length,
        stamps: stamps,
        completed_weeks: stamps.map(s => s.week),
        percentage: Math.round((stamps.length / 12) * 100)
      };

      res.json({ success: true, progress });
    }
  );
});

// 4. Admin endpoints
app.get('/api/admin/stats', (req, res) => {
  const { admin_key } = req.headers;
  
  if (admin_key !== ADMIN_KEY) {
    return res.status(401).json({ success: false, message: 'Unauthorized' });
  }

  db.all(
    `SELECT 
      COUNT(DISTINCT email) as total_students,
      COUNT(*) as total_stamps,
      week,
      COUNT(*) as week_completions
     FROM stamps 
     GROUP BY week`,
    (err, stats) => {
      if (err) {
        return res.status(500).json({ success: false, message: 'Database error' });
      }
      res.json({ success: true, stats });
    }
  );
});

// 5. Export data for Blackboard
app.get('/api/admin/export', (req, res) => {
  const { admin_key } = req.headers;
  
  if (admin_key !== ADMIN_KEY) {
    return res.status(401).json({ success: false, message: 'Unauthorized' });
  }

  db.all(
    `SELECT 
      s.email,
      GROUP_CONCAT(st.week) as completed_weeks,
      COUNT(st.week) as total_stamps,
      MAX(st.timestamp) as last_activity
     FROM students s
     LEFT JOIN stamps st ON s.email = st.email
     GROUP BY s.email`,
    (err, data) => {
      if (err) {
        return res.status(500).json({ success: false, message: 'Database error' });
      }
      res.json({ success: true, data });
    }
  );
});

app.listen(PORT, () => {
  console.log(`ISYS2001 Passport API running on port ${PORT}`);
});
