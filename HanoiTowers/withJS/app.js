// const { useState, useEffect, useRef } = React;

// function TowersOfHanoi() {
//   const [numDisks, setNumDisks] = useState(3);
//   const [rods, setRods] = useState({ A: [], B: [], C: [] });
//   const [selectedDisk, setSelectedDisk] = useState(null);
//   const [startTime, setStartTime] = useState(null);
//   const [bestTime, setBestTime] = useState(null);
//   const [bgColor, setBgColor] = useState("#ffffff");
//   const canvasRef = useRef(null);
//   const [moves, setMoves] = useState(0);

//   useEffect(() => {
//     resetGame();
//   }, []);

//   const resetGame = () => {
//     setRods({
//       A: Array.from({ length: numDisks }, (_, i) => numDisks - i),
//       B: [],
//       C: [],
//     });
//     setSelectedDisk(null);
//     setStartTime(Date.now());
//     setMoves(0);
//     clearConfetti();
//     document.querySelector(".congrats").style.display = "none";
//   };

//   const handleDiskClick = (rod) => {
//     if (selectedDisk) {
//       if (moveDisk(selectedDisk.rod, rod)) {
//         setMoves(moves + 1);
//         setSelectedDisk(null);
//         drawRods();
//         checkWin();
//       }
//     } else if (rods[rod].length > 0) {
//       setSelectedDisk({ rod, disk: rods[rod][rods[rod].length - 1] });
//     }
//   };

//   const moveDisk = (fromRod, toRod) => {
//     if (!rods[fromRod].length) return false;
//     const disk = rods[fromRod][rods[fromRod].length - 1];
//     if (!rods[toRod].length || rods[toRod][rods[toRod].length - 1] > disk) {
//       const newRods = { ...rods };
//       newRods[fromRod].pop();
//       newRods[toRod].push(disk);
//       setRods(newRods);
//       return true;
//     }
//     return false;
//   };

//   const checkWin = () => {
//     if (rods.C.length === numDisks) {
//       const endTime = Date.now();
//       const elapsedTime = (endTime - startTime) / 1000;
//       if (!bestTime || elapsedTime < bestTime) setBestTime(elapsedTime);
//       document.querySelector(".congrats").style.display = "block";
//       dropConfetti();
//     }
//   };

//   const drawRods = () => {
//     const canvas = canvasRef.current;
//     const ctx = canvas.getContext("2d");
//     ctx.clearRect(0, 0, canvas.width, canvas.height);

//     const rodPositions = { A: 100, B: 300, C: 500 };
//     const rodHeight = 300;
//     const rodWidth = 10;

//     Object.keys(rodPositions).forEach((rod) => {
//       const x = rodPositions[rod];
//       ctx.fillStyle = "#000";
//       ctx.fillRect(x - rodWidth / 2, 50, rodWidth, rodHeight);

//       rods[rod].forEach((disk, i) => {
//         const diskHeight = 20;
//         const diskWidth = 20 * disk;
//         ctx.fillStyle = `hsl(${(disk / numDisks) * 360}, 100%, 50%)`;
//         ctx.fillRect(
//           x - diskWidth / 2,
//           rodHeight - (i + 1) * diskHeight,
//           diskWidth,
//           diskHeight
//         );
//       });
//     });
//   };

//   const handleCanvasClick = (e) => {
//     const rect = canvasRef.current.getBoundingClientRect();
//     const x = e.clientX - rect.left;
//     const rod = getRod(x);
//     if (rod) handleDiskClick(rod);
//   };

//   const getRod = (x) => {
//     if (50 <= x && x <= 150) return "A";
//     if (250 <= x && x <= 350) return "B";
//     if (450 <= x && x <= 550) return "C";
//     return null;
//   };

//   const handleColorChange = (e) => {
//     setBgColor(e.target.value);
//     canvasRef.current.style.backgroundColor = e.target.value;
//   };

//   const dropConfetti = () => {
//     const confettiCount = 100;
//     for (let i = 0; i < confettiCount; i++) {
//       const confetti = document.createElement("div");
//       confetti.className = "confetti";
//       confetti.style.left = `${Math.random() * window.innerWidth}px`;
//       confetti.style.backgroundColor = `hsl(${Math.random() * 360}, 100%, 50%)`;
//       document.body.appendChild(confetti);
//     }
//   };

//   const clearConfetti = () => {
//     const confetti = document.querySelectorAll(".confetti");
//     confetti.forEach((el) => el.remove());
//   };

//   useEffect(() => {
//     drawRods();
//   }, [rods]);

//   return (
//     <div>
//       <div className="controls">
//         <label>Number of Disks: </label>
//         <input
//           type="number"
//           value={numDisks}
//           min="1"
//           onChange={(e) => setNumDisks(parseInt(e.target.value))}
//         />
//         <button onClick={resetGame}>Start Game</button>
//         <input type="color" value={bgColor} onChange={handleColorChange} />
//       </div>
//       <canvas
//         ref={canvasRef}
//         width="600"
//         height="400"
//         onClick={handleCanvasClick}
//         style={{ backgroundColor: bgColor }}
//       ></canvas>
//       <div className="congrats">Congratulations! 🎉</div>
//     </div>
//   );
// }

// ReactDOM.render(<TowersOfHanoi />, document.getElementById("root"));

const { useState, useEffect, useRef } = React;

function TowersOfHanoi() {
  const [numDisks, setNumDisks] = useState(3);
  const [rods, setRods] = useState({ A: [], B: [], C: [] });
  const [selectedDisk, setSelectedDisk] = useState(null);
  const [startTime, setStartTime] = useState(null);
  const [bestTime, setBestTime] = useState(null);
  const [bgColor, setBgColor] = useState("#ffffff");
  const [moves, setMoves] = useState([]);
  const canvasRef = useRef(null);

  useEffect(() => {
    resetGame();
  }, []);

  const resetGame = () => {
    const initialRods = {
      A: Array.from({ length: numDisks }, (_, i) => numDisks - i),
      B: [],
      C: [],
    };
    setRods(initialRods);
    setSelectedDisk(null);
    setStartTime(Date.now());
    setMoves([initialRods]);
    clearConfetti();
    document.querySelector(".congrats").style.display = "none";
  };

  const handleDiskClick = (rod) => {
    if (selectedDisk) {
      if (moveDisk(selectedDisk.rod, rod)) {
        const newMoves = [...moves];
        newMoves.push(JSON.parse(JSON.stringify(rods)));
        setMoves(newMoves);
        setSelectedDisk(null);
        drawRods();
        checkWin();
      }
    } else if (rods[rod].length > 0) {
      setSelectedDisk({ rod, disk: rods[rod][rods[rod].length - 1] });
    }
  };

  const moveDisk = (fromRod, toRod) => {
    if (!rods[fromRod].length) return false;
    const disk = rods[fromRod][rods[fromRod].length - 1];
    if (!rods[toRod].length || rods[toRod][rods[toRod].length - 1] > disk) {
      const newRods = { ...rods };
      newRods[fromRod].pop();
      newRods[toRod].push(disk);
      setRods(newRods);
      return true;
    }
    return false;
  };

  const handleBack = () => {
    if (moves.length > 1) {
      const newMoves = moves.slice(0, -1);
      setMoves(newMoves);
      setRods(newMoves[newMoves.length - 1]);
      drawRods();
    }
  };

  const checkWin = () => {
    if (rods.C.length === numDisks) {
      const endTime = Date.now();
      const elapsedTime = (endTime - startTime) / 1000;
      if (!bestTime || elapsedTime < bestTime) setBestTime(elapsedTime);
      document.querySelector(".congrats").style.display = "block";
      dropConfetti();
    }
  };

  const drawRods = () => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const rodPositions = { A: 100, B: 300, C: 500 };
    const rodHeight = 300;
    const rodWidth = 10;

    Object.keys(rodPositions).forEach((rod) => {
      const x = rodPositions[rod];
      ctx.fillStyle = "#000";
      ctx.fillRect(x - rodWidth / 2, 50, rodWidth, rodHeight);

      rods[rod].forEach((disk, i) => {
        const diskHeight = 20;
        const diskWidth = 20 * disk;
        ctx.fillStyle = `hsl(${(disk / numDisks) * 360}, 100%, 50%)`;
        ctx.fillRect(
          x - diskWidth / 2,
          rodHeight - (i + 1) * diskHeight,
          diskWidth,
          diskHeight
        );
      });
    });
  };

  const handleCanvasClick = (e) => {
    const rect = canvasRef.current.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const rod = getRod(x);
    if (rod) handleDiskClick(rod);
  };

  const getRod = (x) => {
    if (50 <= x && x <= 150) return "A";
    if (250 <= x && x <= 350) return "B";
    if (450 <= x && x <= 550) return "C";
    return null;
  };

  const handleColorChange = (e) => {
    setBgColor(e.target.value);
    canvasRef.current.style.backgroundColor = e.target.value;
  };

  const dropConfetti = () => {
    const confettiCount = 100;
    for (let i = 0; i < confettiCount; i++) {
      const confetti = document.createElement("div");
      confetti.className = "confetti";
      confetti.style.left = `${Math.random() * window.innerWidth}px`;
      confetti.style.backgroundColor = `hsl(${Math.random() * 360}, 100%, 50%)`;
      document.body.appendChild(confetti);
    }
  };

  const clearConfetti = () => {
    const confetti = document.querySelectorAll(".confetti");
    confetti.forEach((el) => el.remove());
  };

  useEffect(() => {
    drawRods();
  }, [rods]);

  return (
    <div>
      <div className="controls">
        <label>Number of Disks: </label>
        <input
          type="number"
          value={numDisks}
          min="1"
          onChange={(e) => setNumDisks(parseInt(e.target.value))}
        />
        <button onClick={resetGame}>Start Game</button>
        <input type="color" value={bgColor} onChange={handleColorChange} />
        <button onClick={handleBack}>Undo Move</button>
      </div>
      <canvas
        ref={canvasRef}
        width="600"
        height="400"
        onClick={handleCanvasClick}
        style={{ backgroundColor: bgColor }}
      ></canvas>
      <div className="congrats">Congratulations! 🎉</div>
    </div>
  );
}

ReactDOM.render(<TowersOfHanoi />, document.getElementById("root"));
