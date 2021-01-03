import ListGroup from "react-bootstrap/ListGroup";
import Card from "react-bootstrap/Card";
import React from "react";

function Words(props) {
    const {board, setHighlights} = props

    return (
        <Card.Body className={"overflow-auto"} style={{height: "10em"}}>
            <ListGroup>
                {Object.entries(board.words).map(
                    ([word, coord]) =>
                        <li style={{listStyleType: "none"}}
                            onClick={() => setHighlights(coord)}>
                            {word}
                        </li>
                )}
            </ListGroup>
            <p className={"mt-3"}>Found in {board.time}ms</p>
        </Card.Body>
    )
}

export default Words;