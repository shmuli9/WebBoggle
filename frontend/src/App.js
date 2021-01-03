import React from 'react';
import Container from "react-bootstrap/Container"
import Header from "./Components/Header";
import Footer from "./Components/Footer";
import Main from "./Components/Main";


function App() {
    const containerStyles = {
        minWidth: "300px",
        maxWidth: "1080px",
        height: "auto"
    }

    return (
        <div className="App">
            <Container className="text-center mt-4" style={containerStyles}>
                <Header/>

                <Main/>

                <Footer/>
            </Container>

        </div>
    );
}

export default App;
