import React, { useEffect } from 'react';
import { Network } from 'vis-network';
import { DataSet } from 'vis-data';
import axios from 'axios';
import { useState } from 'react';

const GraphVisualization = ({ nodes, edges }) => {
    const [neighbors, setNeighbors] = useState([]);
    const [selectedNodeLabel, setSelectedNodeLabel] = useState('');

    const transformNodes = (nodes) => {
        return nodes?.map(node => ({  // thenga ensures the function is called only when nodes exist
            id: node.id,
            label: `${node.label} - ${node.value.toFixed(2)}`,
        }));
    }
    useEffect(() => {
        const container = document.getElementById('network');
        const nodesWithRank = transformNodes(nodes); 
        const data = {
            nodes: new DataSet(nodesWithRank),
            edges: new DataSet(edges),
        };
        const options = {
            // Add any specific visualization options you want
        };
        const network = new Network(container, data, options);

        network.on('click', async (params) => {
            if (params.nodes.length > 0) {
                const nodeId = params.nodes[0];
                const selectedNode = nodes.find(node => node.id === nodeId);
                setSelectedNodeLabel(selectedNode.label);
                try {
                    const response = await axios.get(`/api/get_neighbors/${nodeId}`);
                    const neighbors = response.data;
                    setNeighbors(neighbors);
                } catch (error) {
                    console.error('Error fetching neighbors:', error);
                }
            }
        });
        network.on('deselectNode', () => {
            setSelectedNodeLabel('');
            setNeighbors([]);
        });
    }, [nodes, edges]);

    return (
        <div>
        <div id="network" style={{ height: '600px' }} />
        {selectedNodeLabel && (
                <div style={{ 
                    position: 'absolute', 
                    top: 0, 
                    left: 0, 
                    backgroundColor: 'rgba(0, 0, 0, 0.1)', 
                    padding: '10px', 
                    borderRadius: '5px' 
                }}>
                    <h3>Neighbors of {selectedNodeLabel}:</h3>
                    <ul style={{ listStyleType: 'none', padding: 0 }}>
                        {neighbors.map(neighbor => (
                            <li key={neighbor.id}>{`${neighbor.label}: ${neighbor.value.toFixed(2)}`}</li>
                        ))}
                    </ul>
                </div>
            )}
    </div>
    );
};

export default GraphVisualization;
