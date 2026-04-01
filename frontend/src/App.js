import React from 'react';

function Login() {
    return (
        <div>
            <h2>Login</h2>
            {/* Login form goes here */}
        </div>
    );
}

function Dashboard() {
    return (
        <div>
            <h2>Dashboard</h2>
            {/* Dashboard components go here */}
        </div>
    );
}

function App() {
    return (
        <div className="App">
            <Login />
            <Dashboard />
        </div>
    );
}

export default App;