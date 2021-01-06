import ListGroup from "react-bootstrap/ListGroup";
import Card from "react-bootstrap/Card";
import {useState} from "react";
import {FormControl, InputGroup, NavLink} from "react-bootstrap";
import Accordion from "react-bootstrap/Accordion";
import Button from "react-bootstrap/Button";
import _ from "underscore";
import "../Styles/Words.css"

function Words(props) {
    const {board, setHighlights} = props
    const [query, setQuery] = useState("")
    const [activeWord, setActiveWord] = useState("")
    const [sortByLen, setSortBy] = useState(false)

    const setActiveHighlights = (word, coord) => {
        setActiveWord(word)
        setHighlights(coord)
    }

    const numWords = _.size(board.words)
    const filteredWords = Object.entries(board.words).filter((word) => word[0].includes(query.trim()))
    const sizeFiltered = _.size(filteredWords)
    const sortedByLen = [...filteredWords].sort((f, s) => s[0].length - f[0].length)

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
                    <Card.Body className={"overflow-auto"} style={{maxHeight: "68vh"}}>
                        <InputGroup className={"mb-3"}>
                            <FormControl value={query} onChange={e => setQuery(e.target.value.toUpperCase())}
                                         style={{textTransform: "uppercase"}} placeholder={"SEARCH"}/>
                            <InputGroup.Append>
                                <InputGroup.Text>{sizeFiltered}/{numWords} results</InputGroup.Text>
                            </InputGroup.Append>
                        </InputGroup>

                        <Button variant={"success"} className={"mb-3"} disabled={sizeFiltered < 1}
                                onClick={() => setSortBy((old) => !old)}>
                            Sort {sortByLen ? "Alphabetically" : "by Length"}
                        </Button>


                        <ListGroup variant={"flush"} style={{height: "45vh", overflowY: "auto"}}>
                            {(sortByLen ? sortedByLen : filteredWords).map(([word, coord]) =>
                                <ListGroup.Item
                                    onClick={() => word === activeWord ? setActiveHighlights("", []) : setActiveHighlights(word, coord)}
                                    active={word === activeWord} action as={NavLink}>
                                    {word}
                                </ListGroup.Item>
                            )}
                        </ListGroup>

                        <p className={"mt-3"}>Words found in {board.time}ms<br/>Correct as per Collins Scrabble
                            Dictionary 2019</p>
                    </Card.Body>
                </Accordion.Collapse>
            </Card>
        </Accordion>

    )
}

export default Words;