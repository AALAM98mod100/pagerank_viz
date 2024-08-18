import React, { useState, useEffect, useMemo } from 'react';
import axios from 'axios';
import Button from '@mui/material/Button';
import AddGraphModal from './AddGraphModal';


const GraphIndex = ({ graphArray, setGraphArray, setGraphData }) => {
  const [showAddGraphModal, setShowAddGraphModal] = useState(false);

  useEffect(() => {
    // Fetch the initial graph data from the backend
    axios.get('/api')
      .then(response => {
        setGraphArray(response.data);
      })
      .catch(error => console.error('Error fetching graph data:', error));
  }, []);


  const getGraphData = (graph_id) => {
    axios.get(`/api/get_graph/${graph_id}`)
      .then(response => {
        setGraphData(response.data);
      })
      .catch(error => console.error('Error fetching graph data:', error));
  };

  const renderGraphButtons = useMemo(
    () => {
      return (
        <div style={
          {
            display: 'flex',
            flexDirection: 'column',
            gap: '1rem',
            padding: '1rem',
          }
        }>
          <ol>
            {graphArray.map((graph, index) => (
              <li key={index}>
                <Button style={
                  {
                    width: '100%',
                    height: '3rem',
                  }
                }  variant="outlined" onClick={() => getGraphData(graph.id)}>
                  {graph.name || "Default Name"}
                </Button>
              </li>
            ))}
          </ol>
          <Button variant="contained" onClick={() => setShowAddGraphModal(true)}> 
            Add New Graph
        </Button>
          {
            showAddGraphModal && <AddGraphModal setGraphData={setGraphData} setGraphArray={setGraphArray} handleClose={() => setShowAddGraphModal(false)}/>
        }
        </div>
      );
    },
    [graphArray, showAddGraphModal]
  );

  return (
    <div style={
      {
        border: '1px solid black',
      }
    }>
      {renderGraphButtons}
    </div>

  );
};

export default GraphIndex;
