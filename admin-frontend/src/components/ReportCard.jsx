import React from 'react'

const ReportCard = ({ report }) => {
  const { machine_id, timestamp, report: data } = report

  const isCompliant = data.disk_encrypted && data.system_updated && data.antivirus_present

  return (
    <div className={\`p-4 rounded-lg shadow \${isCompliant ? 'bg-green-100' : 'bg-red-100'}\`}>
      <h2 className="text-lg font-semibold">{machine_id}</h2>
      <p className="text-sm text-gray-600">{new Date(timestamp).toLocaleString()}</p>
      <ul className="mt-2 text-sm">
        <li>Disk Encrypted: {data.disk_encrypted ? "✅" : "❌"}</li>
        <li>System Updated: {data.system_updated ? "✅" : "❌"}</li>
        <li>Antivirus Present: {data.antivirus_present ? "✅" : "❌"}</li>
        <li>Sleep Settings: {data.sleep_settings}</li>
      </ul>
    </div>
  )
}

export default ReportCard
