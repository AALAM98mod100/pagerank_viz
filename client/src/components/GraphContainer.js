import React, { useState } from 'react';
import GraphVisualization from './GraphVisualization';
import axios from 'axios';
import AddNodeModal from './AddNodeModal';
import AddEdgeModal from './AddEdgeModal';
import Button from '@mui/material/Button';



const GraphContainer = ({graphData, setGraphData}) => {
    const [showAddNodeModal, setShowAddNodeModal] = useState(false);
    const [showAddEdgeModal, setShowAddEdgeModal] = useState(false);
    const [error, setError] = useState(null);
    
    const calculatePageRank = () => {
        axios.get(`/api/calculate_pagerank/${graphData.id}`)
            .then(response => {
                setGraphData(response.data);
                setError(null); // Reset error state
            })
            .catch(error => console.error('Error fetching graph data:', error));
            setError('Failed to fetch graph data. Please try again.');
    };

    return (
        <div style={{
            position: 'relative',
            display: 'flex',
            flexDirection: 'column',  // Corrected from 'direction' to 'flexDirection'
            alignItems: 'flex-end',  // Center align items horizontally
            justifyContent: 'center',  // Center align items vertically
            padding: '2px',
            border: '1px solid black',
        }}>
            {error && <div style={{ color: 'red', position: 'relative' }}>{error}</div>}
        <div style={{
            position: 'absolute',
            top: '1px',
            right: '1px',
            display: 'flex',
            flexDirection: 'column',
            gap: '1rem',
            zIndex: 1
        }}>
        <Button disabled={!graphData?.id} variant="contained" onClick={calculatePageRank}> 
            Calculate PageRank 
        </Button>
        <Button disabled={!graphData?.id} variant="contained" onClick={() => setShowAddNodeModal(true)}> 
            Add Node 
        </Button>
        <Button disabled={!graphData?.id} variant="contained" onClick={() => setShowAddEdgeModal(true)}> 
            Add Edge
        </Button>
        </div>
        <GraphVisualization nodes={graphData.nodes} edges={graphData.edges} />
        {
            showAddNodeModal && <AddNodeModal graphData={graphData} setGraphData={setGraphData} handleClose={() => setShowAddNodeModal(false)}/>
        }
        {
            showAddEdgeModal && <AddEdgeModal graphData={graphData} setGraphData={setGraphData} handleClose={() => setShowAddEdgeModal(false)}/>
        }
    </div>
    );
};

export default GraphContainer;
