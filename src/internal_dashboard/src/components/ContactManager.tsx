import React, { useState, useEffect } from 'react';

const ContactManager = () => {
    const [contacts, setContacts] = useState([]);

    useEffect(() => {
        fetch('/api/contacts')
            .then(response => response.json())
            .then(data => setContacts(data));
    }, []);

    return (
        <div>
            <h2>Contacts</h2>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Phone Number</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {contacts.map((contact: any) => (
                        <tr key={contact.id}>
                            <td>{contact.name}</td>
                            <td>{contact.phone_number}</td>
                            <td>{contact.status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ContactManager;
