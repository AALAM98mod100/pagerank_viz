import React from 'react';

import { useState } from 'react';
import GraphContainer from './components/GraphContainer';
import GraphIndex from './components/GraphIndex';
import { ThemeProvider } from '@mui/material';
import theme from './assets/theme';

const App = () => {
    const [graphArray, setGraphArray] = useState([]);
    const [graphData, setGraphData] = useState({});
    return (
        <ThemeProvider theme={theme}>
        <div className="App">
            <h1>Graph Visualization and PageRank</h1>
            <div style={
            {
                display: 'flex',
                flexDirection: 'row',
            }
        }>
        <GraphIndex graphArray={graphArray} setGraphArray={setGraphArray} setGraphData={setGraphData}/>
        <GraphContainer graphData={graphData} setGraphData={setGraphData}/> 
        </div>
        </div>
        </ThemeProvider>
    );
};

export default App;
