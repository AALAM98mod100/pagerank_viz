import React, { useEffect } from 'react';
import { Network } from 'vis-network';
import { DataSet } from 'vis-data';

const GraphVisualization = ({ nodes, edges }) => {
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
        new Network(container, data, options);
    }, [nodes, edges]);

    return (
        <div id="network" style={{ height: '600px' }} />
    );
};

export default GraphVisualization;
