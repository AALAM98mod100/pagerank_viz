import React from 'react';

import { useState } from 'react';
import GraphContainer from './components/GraphContainer';
import GraphIndex from './components/GraphIndex';
import { ThemeProvider } from '@mui/material';
import theme from './assets/theme';
import HelpText from './components/HelpText';

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
        <div style={
            {
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'center',
                alignItems: 'center',
                width: '20%',
                padding: '20px',
            }
        }>
        <HelpText />
        </div>
        </div>
        </div>
        </ThemeProvider>
    );
};

export default App;
