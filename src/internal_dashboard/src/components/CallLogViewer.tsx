import React, { useState, useEffect } from 'react';

const CallLogViewer = () => {
    const [callLogs, setCallLogs] = useState([]);

    useEffect(() => {
        fetch('/api/calls')
            .then(response => response.json())
            .then(data => setCallLogs(data));
    }, []);

    return (
        <div>
            <h2>Call Logs</h2>
            <table>
                <thead>
                    <tr>
                        <th>Caller Role</th>
                        <th>Customer Number</th>
                        <th>Duration (s)</th>
                        <th>Recording</th>
                    </tr>
                </thead>
                <tbody>
                    {callLogs.map((log: any) => (
                        <tr key={log.id}>
                            <td>{log.caller_role}</td>
                            <td>{log.customer_number}</td>
                            <td>{log.duration_seconds}</td>
                            <td>
                                <a href={log.recording_url} target="_blank" rel="noopener noreferrer">Listen</a>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default CallLogViewer;
