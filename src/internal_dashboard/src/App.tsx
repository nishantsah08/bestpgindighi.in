import React, { useState } from 'react';
import CallLogViewer from './components/CallLogViewer';
import ContactManager from './components/ContactManager';
import TranscriptDetailView from './components/TranscriptDetailView';

const App = () => {
    const [view, setView] = useState('calls');
    const [selectedCall, setSelectedCall] = useState(null);

    const handleSelectCall = (call: any) => {
        setSelectedCall(call);
        setView('transcript');
    };

    const handleBack = () => {
        setSelectedCall(null);
        setView('calls');
    };

    const renderView = () => {
        switch (view) {
            case 'calls':
                return <CallLogViewer onSelectCall={handleSelectCall} />;
            case 'contacts':
                return <ContactManager />;
            case 'transcript':
                return <TranscriptDetailView call={selectedCall} onBack={handleBack} />;
            default:
                return <CallLogViewer onSelectCall={handleSelectCall} />;
        }
    };

    return (
        <div>
            <nav>
                <button onClick={() => setView('calls')}>Call Logs</button>
                <button onClick={() => setView('contacts')}>Contacts</button>
            </nav>
            {renderView()}
        </div>
    );
};

export default App;