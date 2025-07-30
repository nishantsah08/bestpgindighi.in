import React, { useState, useEffect } from 'react';

const CallLogViewer = ({ onSelectCall }: { onSelectCall: (call: any) => void }) => {
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
                        <th>Status</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    {callLogs.map((log: any) => (
                        <tr key={log.id}>
                            <td>{log.caller_role}</td>
                            <td>{log.customer_number}</td>
                            <td>{log.duration_seconds}</td>
                            <td>{log.transcription_status}</td>
                            <td>
                                {log.transcription_status === 'COMPLETED' && (
                                    <button onClick={() => onSelectCall(log)}>View</button>
                                )}
                                {log.transcription_status === 'FAILED' && (
                                    <button>Re-try</button>
                                )}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default CallLogViewer;