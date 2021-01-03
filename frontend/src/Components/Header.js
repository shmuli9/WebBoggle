import Alert from "react-bootstrap/Alert";
import React from "react";

function Header() {
    return (
        <Alert variant={"primary"}>
            <a className="h2 alert-heading" href="/">WebBoggle</a>
            <hr/>
            <p className={"mb-0"}>
                Generate boggle boards and share them with your friends so that you can play remotely!
            </p>
        </Alert>
    )
}

export default Header;