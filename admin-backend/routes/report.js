const express = require('express');
const router = express.Router();
const Report = require('../models/Report');

router.post('/', async (req, res) => {
  try {
    const report = new Report(req.body);
    await report.save();
    res.status(200).json({ message: 'Report saved' });
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

router.get('/', async (req, res) => {
  const reports = await Report.find().sort({ timestamp: -1 }).limit(100);
  res.json(reports);
});

module.exports = router;
