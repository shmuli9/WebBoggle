import ListGroup from "react-bootstrap/ListGroup";
import Card from "react-bootstrap/Card";
import React from "react";

function Words(props) {
    const {words, setHighlights} = props

    const highlightBoard = (coords) => {
        let h = Array(4).fill(null).map(() => Array(4).fill(false));

        for (const c in coords) {
            let [x, y] = coords[c].split(",")
            h[x][y] = true
        }

        setHighlights(h)
    }

    return (
        <Card.Body className={"overflow-auto"} style={{height: "10em"}}>
            <ListGroup>
                {Object.entries(words).map(
                    ([word, coord]) =>
                        <li style={{listStyleType: "none"}}
                            onClick={() => highlightBoard(coord)}>
                            {word}
                        </li>
                )}
            </ListGroup>
            <p className={"mt-3"}>Found in 1.5ms</p>
        </Card.Body>
    )
}

export default Words;