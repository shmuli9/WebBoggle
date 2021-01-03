import React, {useEffect, useState} from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Board from "./Board";
import Words from "./Words";
import Accordion from "react-bootstrap/Accordion";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import _ from "underscore";
import Alert from "react-bootstrap/Alert";
import InputGroup from "react-bootstrap/InputGroup";
import FormControl from "react-bootstrap/FormControl";

function Main() {
    const [boardID, setBoardID] = useState("");
    const [words, setWords] = useState(Array(1).fill(""));
    const [dice, setDice] = useState(Array(4).fill(Array(4).fill("")));
    const [highlights, setHighlights] = useState(Array(4).fill(Array(4).fill(false)));

    useEffect(() => {
        get_board()
    }, []);

    const newBoard = () => {
        get_board()
    }

    const get_board = () => {
        fetch('/generate_board', {method: "POST"}).then(res => res.json()).then(data => {
            setBoardID(data.game_id);
            setDice(data.board);
            setWords(data.words);
            setHighlights()
        });
    }

    return (
        <>
            <Row className="mt-5">
                <Col sm={4} className={"my-auto"}></Col>
                <Board dice={dice} highlights={highlights}/>
                <Col sm={4} className={"my-auto"}>
                    <Accordion>
                        <Card>
                            <Card.Header>
                                <h2 className={"mb-0"}>
                                    <Accordion.Toggle as={Button} variant={"link"} eventKey={"0"}>
                                        <b>Valid Words</b>
                                        <span id={"word_count"}> ({_.size(words)})</span>
                                    </Accordion.Toggle>
                                </h2>
                            </Card.Header>
                            <Accordion.Collapse eventKey="0">
                                <Words words={words} setHighlights={setHighlights}/>
                            </Accordion.Collapse>
                        </Card>
                    </Accordion>
                </Col>
            </Row>

            <Button variant={"success"} className={"btn-lg font-weight-bold mt-5"} onClick={newBoard}>
                New Board
            </Button>

            <Alert variant="primary" className="mx-auto m-5" style={{maxWidth: "18rem"}}>
                <label htmlFor="game_link" className={"h5 mb-3"}>Share Game</label>
                <p>
                    <a href={`/join/${boardID}`} className={"font-weight-bold"}>{boardID}</a>
                </p>
                <hr/>
                <label htmlFor="game_code" className="h5 mb-3">Join Game</label>
                <InputGroup className="mb-3">
                    <FormControl
                        placeholder="GAME CODE"
                        id="game_code"
                        maxLength="6"
                        style={{textTransform: "uppercase"}}
                    />
                    <InputGroup.Append>
                        <Button id="join_game" variant={"success"}>Join</Button>
                    </InputGroup.Append>
                </InputGroup>
            </Alert>
        </>
    )
}

export default Main;