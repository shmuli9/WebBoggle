import ListGroup from "react-bootstrap/ListGroup";
import Card from "react-bootstrap/Card";
import {useState} from "react";
import {FormControl, InputGroup, NavLink} from "react-bootstrap";
import Accordion from "react-bootstrap/Accordion";
import Button from "react-bootstrap/Button";
import _ from "underscore";
import "../Styles/Words.css"
import SimpleBars from "simplebar-react";

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

    const wordScore = (word) => {
        const len = word.length

        switch (len) {
            case 3:
            case 4:
                return 1
            case 5:
                return 2
            case 6:
                return 3
            case 7:
                return 5
            default:
                return 11
        }
    }

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
                    <Card.Body className={"overflow-auto"} style={{maxHeight: "66vh"}}>
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

                        <p>Click a word to see it on the Board!</p>

                        <SimpleBars style={{maxHeight: "40vh"}}>
                            <ListGroup variant={"flush"}>
                                {(sortByLen ? sortedByLen : filteredWords).map(([word, coord]) =>
                                    <ListGroup.Item
                                        onClick={() => word === activeWord ? setActiveHighlights("", []) : setActiveHighlights(word, coord)}
                                        active={word === activeWord} action as={NavLink} key={word}>
                                        {word} ({wordScore(word)})
                                    </ListGroup.Item>
                                )}
                            </ListGroup>
                        </SimpleBars>

                        <p className={"mt-3"}>Words found in {board.time}ms<br/>Correct as per Collins Scrabble
                            Dictionary 2019</p>
                    </Card.Body>
                </Accordion.Collapse>
            </Card>
        </Accordion>

    )
}

export default Words;