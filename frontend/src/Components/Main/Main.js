import {useEffect, useState} from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Board from "./Board";
import Words from "./Words";
import Button from "react-bootstrap/Button";
import Alert from "react-bootstrap/Alert";
import {Link, useHistory, useParams} from "react-router-dom";
import Game from "./Game";

function Main() {
    const defaultBoard = {
        id: "XXXXXX",
        dice: Array(4).fill(Array(4).fill(" ")),
        words: [],
        time: ""
    }
    const [board, setBoard] = useState(defaultBoard)
    const [highlights, setHighlights] = useState([]);
    const {game_id} = useParams();
    const history = useHistory()

    useEffect(() => {
        newBoard()
    }, []);

    const newBoard = () => {
        setHighlights([])
        setBoard(defaultBoard)
        fetch(`/api/generate_board/${game_id && game_id}`, {method: "POST"})
            .then(res => res.json())
            .then(data => {
                setBoard({
                    id: data.game_id,
                    dice: data.board,
                    words: data.words,
                    time: data.time_taken
                })
                if (game_id) {
                    history.push("/") // redirect to standard page and clear game_id
                }
            });
    }


    return (
        <>
            <Alert variant={"dark"} className={""}>
                <Link to={"/"} className="h2 alert-heading">WebBoggle</Link>
                <hr/>
                <p className={"mb-0"}>
                    Generate boggle boards and share them with your friends so that you can play remotely!
                </p>
            </Alert>

            <Row className="mt-5">
                <Col sm={4} className={"mb-auto"}>
                    <Game/>
                </Col>

                <Col sm={4} className={"mb-auto"}>
                    <Board dice={board.dice} highlights={highlights}/>
                    <Button variant={"success"} className={"btn-lg font-weight-bold mt-5"} onClick={newBoard}>
                        New Board
                    </Button>

                    <Alert variant="dark" className="mx-auto m-5" style={{maxWidth: "18rem"}}>
                        <label htmlFor="game_link" className={"h5 mb-3"}>Share Game</label>
                        <p>
                            <Link to={`/join/${board.id}`} className={"font-weight-bold"}>{board.id}</Link>
                        </p>
                    </Alert>
                </Col>

                <Col sm={4} className={"mb-auto"}>
                    <Words board={board} setHighlights={setHighlights}/>
                </Col>
            </Row>


        </>
    )
}

export default Main;