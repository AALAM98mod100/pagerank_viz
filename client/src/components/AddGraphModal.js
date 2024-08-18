import React, { useState } from "react";
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';
import TextField from '@mui/material/TextField';
import { Button } from "@mui/material";
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

const AddGraphModal = ({setGraphData, setGraphArray, handleClose}) => {
    const [graphName, setGraphName] = useState("");

    const addGraph = () => {
        console.log("Adding graph");
        axios.post(`/api/create_graph/`, {
            name: graphName,
        }).then(response => {
            console.log(response.data);
            setGraphData(response.data.graph);
            setGraphArray(response.data.graphs);
            handleClose();
        }
        ).catch(error => console.error('Error adding node:',
        error
        ))
    }

    const validateForm = () => {
        return graphName.length > 0;
    }

    const onFormSubmit = (e) => {
        e.preventDefault();
        if (validateForm()) {
            addGraph();
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
          <Typography id="modal-modal-title" variant="h6" component="h2" style={{
              paddingBottom: '1rem'
            }}>
            Type a name for the new graph
          </Typography>
          <div style={
              {
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '1rem',
                }
            }>
          <TextField
          required
          label="Graph Name"
          onChange={(e) => setGraphName(e.target.value)}
          error={!graphName}
          />
        <Button type="submit">
            Create new graph
        </Button>
          </div>
        </Box>
          </form>
      </Modal>
    </div>
    );
    };

export default AddGraphModal;