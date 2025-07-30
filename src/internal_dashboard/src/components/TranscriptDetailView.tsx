import React from 'react';

const TranscriptDetailView = ({ call, onBack }: { call: any, onBack: () => void }) => {
    return (
        <div>
            <button onClick={onBack}>Back to Call Logs</button>
            <h2>Transcript for Call with {call.customer_number}</h2>
            <p>{call.transcript}</p>
        </div>
    );
};

export default TranscriptDetailView;
