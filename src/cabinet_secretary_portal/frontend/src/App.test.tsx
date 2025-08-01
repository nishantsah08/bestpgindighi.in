import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import App from './App';

// Mock scrollIntoView for the ref
const scrollIntoViewMock = jest.fn();
window.HTMLElement.prototype.scrollIntoView = scrollIntoViewMock;

describe('App Component', () => {
  beforeEach(() => {
    scrollIntoViewMock.mockClear();
  });

  test('renders Cabinet Secretary Portal header', () => {
    render(<App />);
    expect(screen.getByText(/Cabinet Secretary Portal/i)).toBeInTheDocument();
    expect(scrollIntoViewMock).toHaveBeenCalled(); // Should be called on initial render
  });

  test('sends a message and displays it', async () => {
    render(<App />);
    const inputElement = screen.getByPlaceholderText(/Type your message.../i);
    const sendButton = screen.getByRole('button', { name: /Send/i });

    const userMessage = 'Hello, AI!';
    userEvent.type(inputElement, userMessage);
    fireEvent.click(sendButton);

    expect(await screen.findByText(userMessage)).toBeInTheDocument();
    expect(inputElement).toHaveValue(''); // Input should be cleared
    expect(scrollIntoViewMock).toHaveBeenCalled(); // Should be called after sending message
  });

  test('displays simulated AI response after user message', async () => {
    render(<App />);
    const inputElement = screen.getByPlaceholderText(/Type your message.../i);
    const sendButton = screen.getByRole('button', { name: /Send/i });

    const userMessage = 'Test AI response';
    userEvent.type(inputElement, userMessage);
    fireEvent.click(sendButton);

    // Expect the initial 'Thinking...' message
    expect(await screen.findByText(/Thinking.../i)).toBeInTheDocument();

    // Wait for the simulated AI response to appear
    expect(await screen.findByText(`AI: ${userMessage}`)).toBeInTheDocument();
    expect(scrollIntoViewMock).toHaveBeenCalled(); // Should be called after AI response
  });
});
