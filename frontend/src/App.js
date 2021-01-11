import {lazy, Suspense} from 'react';
import Container from "react-bootstrap/Container"
import Header from "./Components/Header";
import Footer from "./Components/Footer";
import {BrowserRouter as Router, Redirect, Route, Switch} from "react-router-dom";
import LoadingScreen from "./Components/Loading";
import 'simplebar/dist/simplebar.min.css';
import SimpleBars from "simplebar-react";
import Main from "./Components/Main/Main";


function App() {
    const containerStyles = {
        minWidth: "300px",
        maxWidth: "1080px"
    }

    const About = lazy(() => import("./Components/About/About"));

    return (
        <Router>
            <SimpleBars style={{maxHeight: "100vh",}}>

                <Header/>

                <Suspense fallback={LoadingScreen}>
                    <Container className="text-center mt-4" style={containerStyles}>
                        <Switch>
                            <Route exact path={"/about"}>
                                <About/>
                            </Route>
                            <Route exact path={"/join/:gameID"}
                                   render={({ match }) => <Redirect to={`/${match.params.gameID}`}/>}>
                            </Route>
                            <Route path={["/:gameID", "/"]}>
                                <Main/>
                            </Route>
                        </Switch>
                    </Container>
                </Suspense>

                <Footer/>

            </SimpleBars>
        </Router>
    );
}

export default App;
