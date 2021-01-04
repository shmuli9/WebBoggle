import {Suspense, lazy} from 'react';
import Container from "react-bootstrap/Container"
import Header from "./Components/Header";
import Footer from "./Components/Footer";
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";


function App() {
    const containerStyles = {
        minWidth: "300px",
        maxWidth: "1080px"
    }

    const Main = lazy(() => import("./Components/Main"));
    const About = lazy(() => import("./Components/About"));

    return (
        <Router>
            <div className="App">
                <Header/>

                <Suspense fallback={<div>Loading...</div>}>
                    <Container className="text-center mt-4" style={containerStyles}>
                        <Switch>
                            <Route path={"/about"}>
                                <About/>
                            </Route>
                            <Route path={"/join/:game_id"}>
                                <Main/>
                            </Route>
                            <Route path={"/"}>
                                <Main/>
                            </Route>
                        </Switch>
                    </Container>
                </Suspense>

                <Footer/>
            </div>
        </Router>
    );
}

export default App;
