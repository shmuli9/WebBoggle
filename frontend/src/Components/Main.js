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
import {Link} from "react-router-dom";

function Main() {
    const [board, setBoard] = useState({id: "", dice: "", words: [], time: ""})
    const [highlights, setHighlights] = useState([]);

    useEffect(() => {
        get_board()
    }, []);

    const newBoard = () => {
        get_board()
    }

    const get_board = () => {
        fetch('/generate_board', {method: "POST"}).then(res => res.json()).then(data => {
            setBoard({
                id: data.game_id,
                dice: data.board,
                words: data.words,
                time: data.time_taken
            })
            setHighlights([])
        });
    }

    return (
        <>
            <Alert variant={"dark"} className={""}>
                <a className="h2 alert-heading" href="/">WebBoggle</a>
                <hr/>
                <p className={"mb-0"}>
                    Generate boggle boards and share them with your friends so that you can play remotely!
                </p>
            </Alert>

            <Row className="mt-5">
                <Col sm={4} className={"my-auto"}></Col>
                <Board dice={board.dice} highlights={highlights}/>
                <Col sm={4} className={"my-auto"}>
                    <Accordion>
                        <Card>
                            <Card.Header>
                                <h2 className={"mb-0"}>
                                    <Accordion.Toggle as={Button} variant={"link"} eventKey={"0"}>
                                        <b>Valid Words</b>
                                        <span id={"word_count"}> ({_.size(board.words)})</span>
                                    </Accordion.Toggle>
                                </h2>
                            </Card.Header>
                            <Accordion.Collapse eventKey="0">
                                <Words board={board} words={board.words} setHighlights={setHighlights}/>
                            </Accordion.Collapse>
                        </Card>
                    </Accordion>
                </Col>
            </Row>

            <Button variant={"success"} className={"btn-lg font-weight-bold mt-5"} onClick={newBoard}>
                New Board
            </Button>

            <Alert variant="dark" className="mx-auto m-5" style={{maxWidth: "18rem"}}>
                <label htmlFor="game_link" className={"h5 mb-3"}>Share Game</label>
                <p>
                    <Link to={`/join/${board.id}`} className={"font-weight-bold"}>{board.id}</Link>
                </p>
            </Alert>
        </>
    )
}

export default Main;