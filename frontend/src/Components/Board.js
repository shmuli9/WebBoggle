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
            let die = ""
            for (let j = 0; j < dice[i].length; j++) {
                die = dice[i][j]
                r.push(<td key={`cell-${i}-${j}`} style={
                    highlights ?
                        highlights.find(el => el === `${i},${j}`) ? style : {} : {}}>
                    {die}
                </td>)
            }
            d.push((<tr key={`row${i}`}>{r}</tr>))
        }
        return d
    }

    return (
        <table className="mx-auto border p-2" style={{maxWidth: "16em"}}>
            <tbody id={"board"}>
            {renderBoard()}
            </tbody>
        </table>
    )
}

export default Board;

