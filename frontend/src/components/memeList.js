import React, { Component } from "react";
import { Container } from "reactstrap";
import MemeModal from "./memeModal";
import Card from 'react-bootstrap/Card';
import '../App.css';
import ConfirmRemovalModal from "./confirmRemovalModal";

// show list of memes if present in database
class MemeList extends Component {
  render() {
    const memes = this.props.memes.reverse().slice(0,100);
    return (
      <Container class="list-meme-cards">
        {!memes || memes.length <= 0 ? (
          <b>Ops, no meme posted</b>
        ) : (
            memes.map(memes => (               

            <Container>
              <Card  className="listmemecards" bg='light' border="danger">
              <Card.Title style={{ color: "grey" }}>Posted by: {memes.name}</Card.Title>

              <Card.Header style={{ color: "black" }}>
                    {memes.caption}
                  </Card.Header>
                <Card.Img variant="top" src={memes.url} />
                <Card.Body>
                  
                  {/* go to meme modal if edit meme is clicked */}
                  <MemeModal
                    create={false}
                    memes={memes}
                    resetState={this.props.resetState}
                  />

                  {/* go to confirm removal modal if delete meme is clicked */}
                  &nbsp;&nbsp;
                  <ConfirmRemovalModal
                    id={memes.id}
                    resetState={this.props.resetState}
                  />
                </Card.Body>
              </Card>
            </Container>

           ),
          )
        )}
      </Container>
    );
  }
}

export default MemeList;