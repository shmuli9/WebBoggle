import React from "react";
import "../Styles/table.css"

function Board(props) {
    const {dice, highlights} = props

    const style = {
        background: "blue",
        color: "white"
    }

    const renderBoard = () => {
        let d = []
        for (let i = 0; i < dice.length; i++) {
            let r = []
            for (let j = 0; j < dice[i].length; j++) {
                let die = dice[i][j]
                r.push(<td id={die}
                           style={
                               highlights ?
                                   highlights.find(el => el === `${i},${j}`) ? style : {} : {}}>
                    {die}
                </td>)
            }
            d.push((<tr>{r}</tr>))
        }
        return d
    }

    return (
        <table className="col-sm-4 mx-auto border p-2" style={{maxWidth: "16em"}}>
            <tbody>
            {renderBoard()}
            </tbody>
        </table>
    )
}

export default Board;

