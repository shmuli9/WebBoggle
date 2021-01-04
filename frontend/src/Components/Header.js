import {useState} from "react";
import {Form, FormControl, Nav, Navbar} from "react-bootstrap";
import Button from "react-bootstrap/Button";
import {Link, useHistory} from "react-router-dom";

function Header() {
    const [game, setGame] = useState("")
    const hist = useHistory()

    const joinGame = () => {
        if (game) {
            hist.push(`/join/${game}`)
            setGame("")
        }
    }

    return (
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Navbar.Brand as={Link} to="/">WebBoggle</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
            <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link as={Link} to="/about">About</Nav.Link>
                </Nav>
                <Form inline>
                    <FormControl type="text" placeholder="GAME CODE" maxLength="6"
                                 style={{textTransform: "uppercase"}} className="mr-sm-2"
                                 onChange={e => setGame(e.target.value)} value={game}/>
                    <Button variant="outline-light" onClick={joinGame}>JOIN</Button>
                </Form>
            </Navbar.Collapse>
        </Navbar>
    )
}

export default Header;