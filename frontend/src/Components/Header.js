import React from "react";
import {Form, FormControl, Nav, Navbar} from "react-bootstrap";
import Button from "react-bootstrap/Button";
import {Link} from "react-router-dom";

function Header() {
    return (
        <Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Navbar.Brand as={Link} to="/">WebBoggle</Navbar.Brand>
            <Navbar.Toggle aria-controls="responsive-navbar-nav"/>
            <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="mr-auto">
                    <Nav.Link as={Link} to="/about">About</Nav.Link>
                </Nav>
                <Form inline>
                    <FormControl type="text" placeholder="GAME CODE" className="mr-sm-2"/>
                    <Button variant="outline-light">JOIN</Button>
                </Form>
            </Navbar.Collapse>
        </Navbar>
    )
}

export default Header;