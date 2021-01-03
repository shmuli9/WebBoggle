import ListGroup from "react-bootstrap/ListGroup";
import Card from "react-bootstrap/Card";
import React, {useState} from "react";
import {FormControl, InputGroup} from "react-bootstrap";
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
                    <Card.Body className={"overflow-auto"} style={{height: "12em"}}>
                        <InputGroup className={"mb-3"}>
                            <FormControl value={query} onChange={e => setQuery(e.target.value.toUpperCase())}
                                         style={{textTransform: "uppercase"}}/>
                            <InputGroup.Append>
                                <InputGroup.Text>{_.size(filteredWords)}/{numWords} results</InputGroup.Text>
                            </InputGroup.Append>
                        </InputGroup>

                        <ListGroup variant={"flush"}>
                            {filteredWords.map(([word, coord]) =>
                                    <ListGroup.Item
                                        onClick={() => word === activeWord ? setActiveHighlights("", []) : setActiveHighlights(word, coord)}
                                        active={word === activeWord}>
                                        {word}
                                    </ListGroup.Item>
                                )}
                        </ListGroup>

                        <p className={"mt-3"}>Found in {board.time}ms</p>
                    </Card.Body>
                </Accordion.Collapse>
            </Card>
        </Accordion>

    )
}

export default Words;