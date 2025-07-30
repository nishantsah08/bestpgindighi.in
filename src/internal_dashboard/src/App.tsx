import React, { useState } from 'react';
import CallLogViewer from './components/CallLogViewer';
import ContactManager from './components/ContactManager';

const App = () => {
    const [view, setView] = useState('calls');

    return (
        <div>
            <nav>
                <button onClick={() => setView('calls')}>Call Logs</button>
                <button onClick={() => setView('contacts')}>Contacts</button>
            </nav>
            {view === 'calls' ? <CallLogViewer /> : <ContactManager />}
        </div>
    );
};

export default App;
