const mongoose = require('mongoose');

const reportSchema = new mongoose.Schema({
  machine_id: String,
  timestamp: { type: Date, default: Date.now },
  report: {
    disk_encrypted: Boolean,
    system_updated: Boolean,
    antivirus_present: Boolean,
    sleep_settings: String,
  }
});

module.exports = mongoose.model('Report', reportSchema);
