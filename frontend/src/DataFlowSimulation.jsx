import React, { useState, useEffect } from "react";

function Arrow({ rotation = 0 }) {
  return (
    <svg
      className="w-4 h-4"
      style={{ transform: `rotate(${rotation}deg)` }}
      viewBox="0 0 24 24"
      fill="none"
      stroke="white"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <line x1="5" y1="12" x2="19" y2="12" />
      <polyline points="12,5 19,12 12,19" />
    </svg>
  );
}

export default function DataFlowSimulation() {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setRows((prevRows) => {
        const newRow = { id: Date.now(), text: "Incoming data..." };
        const updatedRows = [...prevRows, newRow];
        if (updatedRows.length > 10) updatedRows.shift();
        return updatedRows;
      });
    }, 750);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="relative min-h-screen bg-gradient-to-br from-gray-100 to-gray-300 flex items-center justify-center overflow-hidden">
      {/* Central white data box */}
      <div className="relative w-[400px] h-[240px] bg-white rounded-xl shadow-2xl border-4 border-red-200 animate-pulse-slow z-10 overflow-hidden">
        <div className="absolute inset-0 flex flex-col justify-end p-2 space-y-1 overflow-hidden">
          {rows.map((row, index) => (
            <div
              key={row.id}
              className="px-3 py-1 text-sm text-gray-800 bg-gray-100/70 rounded-md backdrop-blur-sm animate-slideFade blur-[1.5px]"
              style={{ animationDelay: `${index * 60}ms` }}
            >
              {row.text}
            </div>
          ))}
        </div>
      </div>

      {/* Six animated pulsing data sources with arrows */}
      {[
        { top: "10%", left: "10%", rotation: 45 },
        { top: "10%", right: "10%", rotation: 135 },
        { top: "50%", right: "5%", rotation: 180 },
        { bottom: "10%", right: "10%", rotation: 225 },
        { bottom: "10%", left: "10%", rotation: 315 },
        { top: "50%", left: "5%", rotation: 0 },
      ].map((src, i) => (
        <div key={i} className="absolute" style={src}>
          <div className="w-7 h-7 bg-red-500 rounded-full flex items-center justify-center animate-ping-slow">
            <Arrow rotation={src.rotation} />
          </div>
        </div>
      ))}

      {/* Custom animations */}
      <style>{`
        @keyframes slideFade {
          0% {
            opacity: 0;
            transform: translateY(10px);
          }
          100% {
            opacity: 1;
            transform: translateY(0);
          }
        }
        .animate-slideFade {
          animation: slideFade 0.4s ease-out both;
        }
        @keyframes pulseSlow {
          0%, 100% {
            box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.5);
          }
          50% {
            box-shadow: 0 0 0 8px rgba(239, 68, 68, 0);
          }
        }
        .animate-ping-slow {
          animation: pulseSlow 2s infinite;
        }
        @keyframes pulseBox {
          0%, 100% {
            border-color: rgba(239, 68, 68, 0.2);
          }
          50% {
            border-color: rgba(239, 68, 68, 0.6);
          }
        }
        .animate-pulse-slow {
          animation: pulseBox 3s infinite;
        }
      `}</style>
    </div>
  );
}
