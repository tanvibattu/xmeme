import React, { Component, Fragment } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import EditForm from "./editform";

class MemeModal extends Component {
  state = {
    modal: false
  };

  toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  };

  render() {

    var button = <Button onClick={this.toggle}>Edit</Button>;
    
    return (
      <Fragment>
        {button}
        <Modal isOpen={this.state.modal} toggle={this.toggle}>
          <ModalHeader toggle={this.toggle}>Edit meme</ModalHeader>

            {/* got to edit form to show edit form */}
          <ModalBody>
            <EditForm
              resetState={this.props.resetState}
              toggle={this.toggle}
              memes={this.props.memes}
            />
          </ModalBody>
        </Modal>
      </Fragment>
    );
  }
}

export default MemeModal;

