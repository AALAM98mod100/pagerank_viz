import React from 'react';

const HelpText = () => {
    return (
        <div className="help-text-container">
            <h2>How to Interact with the App</h2>
            <p>
                <strong>Adding a new graph:</strong> To add a new graph, click on the "Add Graph" button and follow the prompts to provide the necessary information.
            </p>
            <p>
                <strong>Adding nodes and edges:</strong> To add nodes and edges to the graph, use the provided tools in the app's toolbar. Click on the "Add Node" button to add a new node, and click on the "Add Edge" button to connect nodes with edges.
            </p>
            <p>
                <strong>Calculating pagerank:</strong> To calculate the pagerank of the graph, click on the "Calculate Pagerank" button. The app will perform the necessary calculations and display the results.
            </p>
            <p>
                <strong>Viewing neighbors:</strong> To view the neighbors of a specific node, simply click on the node in the graph. The app will highlight the neighboring nodes and display their information.
            </p>
        </div>
    );
};

export default HelpText;