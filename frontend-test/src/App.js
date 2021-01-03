import React, {useEffect, useState} from 'react';
import './App.css';
import "./table.css"
import Container from "react-bootstrap/Container"
import Alert from "react-bootstrap/Alert"
import ListGroup from "react-bootstrap/ListGroup"
import Row from "react-bootstrap/Row"
import Col from "react-bootstrap/Col"
import InputGroup from "react-bootstrap/InputGroup"
import FormControl from "react-bootstrap/FormControl"
import Button from "react-bootstrap/Button"
import Accordion from "react-bootstrap/Accordion"
import Card from "react-bootstrap/Card"
import _ from "underscore"


function App() {
    const [boardID, setBoardID] = useState("");
    const [words, setWords] = useState(Array(1).fill(""));
    const [dice, setDice] = useState(Array(4).fill(Array(4).fill("")));

    useEffect(() => {
        fetch('/generate_board', {method: "POST"}).then(res => res.json()).then(data => {
            setBoardID(data.game_id);
            setDice(data.board);
            setWords(data.words);
        });
    }, []);

    const newBoard = () => {
        fetch('/generate_board', {method: "POST"}).then(res => res.json()).then(data => {
            setBoardID(data.game_id);
            setDice(data.board);
            setWords(data.words);
        });
    }

    const highlightBoard = (coords) => {
        console.log(coords)

        const style = {
            background: "blue",
            color: "white"
        }
    }

    const renderBoard = () => {
        for (let i = 0; i < dice.length; i++) {
            for (let j = 0; j < dice[i].length; j++){
                let coord = `${i},${j}`
            }
        }
    }

    return (
        <div className="App">
            <Container className="container text-center mt-4"
                       style={
                           {
                               minWidth: "300px",
                               maxWidth: "1080px",
                               height: "auto"
                           }
                       }>
                <Alert variant={"primary"}>
                    <a className="h2 alert-heading" href="/">WebBoggle</a>
                    <hr/>
                    <p className={"mb-0"}>
                        Generate boggle boards and share them with your friends so that you can play remotely!
                    </p>
                </Alert>
                <Row className="mt-5">
                    <Col sm={4} className={"my-auto"}></Col>
                    <table className="col-sm-4 mx-auto border p-2" id="boggle_board" style={{maxWidth: "16em"}}>
                        <tbody>

                        {dice.map((row) =>
                            <tr>
                                {row.map((die) =>
                                    <td id={die}>
                                        {die}
                                    </td>)}
                            </tr>)
                        }
                        </tbody>
                    </table>
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
                                    <Card.Body className={"overflow-auto"} style={{height: "10em"}}>
                                        <ListGroup>
                                            {Object.entries(words).map(
                                                ([word, coord]) =>
                                                    <li style={{listStyleType: "none"}}
                                                        onClick={() => highlightBoard(coord)}>
                                                        {word}
                                                    </li>
                                                //     - {coord ? coord.map((coord) => `${coord} `) : ""}
                                            )}
                                        </ListGroup>
                                        <p className={"mt-3"}>Found in 1.5ms</p>
                                    </Card.Body>
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

                <p className="w-100 text-center" style={{bottom: "0", height: "25px"}}>Copyright
                    <a href="https://github.com/shmuli9/WebBoggle"> WebBoggle</a> 2020 ©
                    <a href="https://github.com/shmuli9">Shmuel Margulies</a>
                </p>
            </Container>

        </div>
    );
}

export default App;
