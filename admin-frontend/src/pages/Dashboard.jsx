import React, { useEffect, useState } from 'react'
import axios from 'axios'
import ReportCard from '../components/ReportCard'

const Dashboard = () => {
  const [reports, setReports] = useState([])
  const [filter, setFilter] = useState("")

  useEffect(() => {
    axios.get('http://localhost:8000/api/report')
      .then(res => setReports(res.data))
      .catch(err => console.error(err))
  }, [])

  const filtered = filter
    ? reports.filter(r => r.machine_id.includes(filter))
    : reports

  return (
    <div>
      <div className="mb-4 flex justify-center">
        <input
          type="text"
          placeholder="Filter by Machine ID"
          className="border p-2 rounded w-full max-w-md"
          value={filter}
          onChange={e => setFilter(e.target.value)}
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {filtered.map((report, index) => (
          <ReportCard key={index} report={report} />
        ))}
      </div>
    </div>
  )
}

export default Dashboard
