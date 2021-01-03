import ListGroup from "react-bootstrap/ListGroup";
import Card from "react-bootstrap/Card";
import React, {useState} from "react";
import {FormControl, InputGroup, NavLink} from "react-bootstrap";
import Accordion from "react-bootstrap/Accordion";
import Button from "react-bootstrap/Button";
import _ from "underscore";

function Words(props) {
    const {board, setHighlights} = props
    const [query, setQuery] = useState("")
    const [activeWord, setActiveWord] = useState("")

    const setActiveHighlights = (word, coord) => {
        setActiveWord(word)
        setHighlights(coord)
    }

    const numWords = _.size(board.words)
    const filteredWords = Object.entries(board.words).filter(([word, coord]) => word.includes(query.trim()))
    const sizeFiltered = _.size(filteredWords)

    return (
        <Accordion>
            <Card>
                <Card.Header>
                    <h2 className={"mb-0"}>
                        <Accordion.Toggle as={Button} variant={"link"} eventKey={"0"}>
                            <b>Valid Words</b>
                            <span id={"word_count"}> ({numWords})</span>
                        </Accordion.Toggle>
                    </h2>
                </Card.Header>

                <Accordion.Collapse eventKey="0">
                    <Card.Body className={"overflow-auto"} style={{height: "68vh"}}>
                        <InputGroup className={"mb-3"}>
                            <FormControl value={query} onChange={e => setQuery(e.target.value.toUpperCase())}
                                         style={{textTransform: "uppercase"}}/>
                            <InputGroup.Append>
                                <InputGroup.Text>{sizeFiltered}/{numWords} results</InputGroup.Text>
                            </InputGroup.Append>
                        </InputGroup>

                        <ListGroup variant={"flush"}>
                            {filteredWords.map(([word, coord]) =>
                                <ListGroup.Item
                                    onClick={() => word === activeWord ? setActiveHighlights("", []) : setActiveHighlights(word, coord)}
                                    active={word === activeWord} action as={NavLink}>
                                    {word}
                                </ListGroup.Item>
                            )}
                        </ListGroup>

                        <p className={"mt-3"}>Words found in {board.time}ms<br/>Correct as per Collins Scrabble Dictionary 2019</p>
                    </Card.Body>
                </Accordion.Collapse>
            </Card>
        </Accordion>

    )
}

export default Words;