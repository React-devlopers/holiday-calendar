import React from 'react';
import useAxios from 'axios-hooks'
import './App.css';

function App() {

    const [{ data, loading, error }, refetch] = useAxios('/api/holidays')

    if (loading) return <p>Loading...</p>
    if (error) return <p>Error!</p>

    return (
        <div>
            <button onClick={refetch}>refetch</button>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    )
}

export default App;
