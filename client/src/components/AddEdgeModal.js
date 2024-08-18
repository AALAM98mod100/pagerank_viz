import React, { useState } from "react";
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import TextField from '@mui/material/TextField';
import { Button } from "@mui/material";
import MenuItem from '@mui/material/MenuItem';
import axios from "axios";


const style = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 400,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
  };

const AddEdgeModal = ({graphData, setGraphData, handleClose}) => {
    const [nodeNameOne, setNodeNameOne] = useState("");
    const [nodeNameTwo, setNodeNameTwo] = useState("");

    const graphId = graphData.id;

    const addEdge = () => {
        console.log("Adding edge");
        axios.post(`/api/add_edge/${graphId}`, {
            nodeOne: nodeNameOne,
            nodeTwo: nodeNameTwo
        }).then(response => {
            console.log(response.data);
            setGraphData(response.data);
            handleClose();
        }
        ).catch(error => console.error('Error adding node:',
        error
        ))
    }

    const validateForm = () => {
        return nodeNameOne.length > 0 && nodeNameTwo.length > 0;
    }

    const onFormSubmit = (e) => {
        e.preventDefault();
        if (validateForm()) {
            addEdge();
            console.log("Valid form");
        } else {
            console.log("Invalid form");
        }
    }

    return (
      <div>
        {/* <Button onClick={handleOpen}>Open modal</Button> */}
        <Modal
          open
          onClose={handleClose}
          aria-labelledby="modal-modal-title"
          aria-describedby="modal-modal-description"
        >
          <form onSubmit={onFormSubmit}>
            <Box sx={style}>
              <Typography id="modal-modal-title" variant="h6" component="h2" style={{ paddingBottom: '1rem' }}>
                Select two nodes to create an edge between them
              </Typography>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
                <TextField
                  defaultValue=""
                  required
                  select
                  label="First node"
                  value={nodeNameOne}
                  onChange={(e) => setNodeNameOne(e.target.value)}
                  error={!nodeNameOne}
                >
                  {graphData.nodes.map((node) => (
                    <MenuItem key={node.id} value={node.label}>
                      <Typography color={"black"} variant="body1">
                      {node.label}
                      </Typography>
                    </MenuItem>
                  ))}
                </TextField>
                <TextField
                  defaultValue=""
                  required
                  select
                  label="Second node"
                  value={nodeNameTwo}
                  onChange={(e) => setNodeNameTwo(e.target.value)}
                  error={!nodeNameTwo}
                >
                  {graphData.nodes.map((node) => { 
                    return (
                    <MenuItem key={node.id} value={node.label}>
                      <Typography> 
                        {node.label}
                      </Typography>
                    </MenuItem>
                  )
                  })}
                </TextField>
                <Button type="submit">Add Edge</Button>
              </div>
            </Box>
          </form>
        </Modal>
      </div>
    );
    };

export default AddEdgeModal;