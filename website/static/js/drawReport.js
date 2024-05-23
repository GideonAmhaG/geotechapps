(function () {
    const canvas = document.getElementById("rectangleCanvas");
    const ctx = canvas.getContext("2d");
    const x = 100;
    const y = 25;
    const width = 100;
    const height = 100;
    const col = 25;
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 1;
    ctx.fillStyle = '#d3d3d3';
    ctx.strokeRect(x, y, width, height); 
    ctx.fillRect(x, y, width, height);
    ctx.fillStyle = 'grey'; 
    ctx.strokeRect(x + ((width * 0.5) - (col * 0.5)), y + ((height * 0.5) - (col * 0.5)), col, col);
    ctx.fillRect(x + ((width * 0.5) - (col * 0.5)), y + ((height * 0.5) - (col * 0.5)), col, col);
    // lines
    const off1 = 10;
    ctx.lineWidth = 0.5;
    ctx.beginPath();
    ctx.moveTo(x + (width * 0.5), y - off1);
    ctx.lineTo(x + (width * 0.5), y + width + off1);
    ctx.moveTo(x - off1, y + (height * 0.5));
    ctx.lineTo(x + width + off1, y + (height * 0.5));
    ctx.stroke();
    // text
    const txtOff1 = 10;
    const fontSize = 13;
    const fontFamily = 'Arial';
    const textColor = 'black';
    function drawText(text, x, y, fontScale, rotation = 0)
    {
        ctx.save(); 
        ctx.translate(x, y); 
        ctx.rotate(rotation * Math.PI / 180); 
        ctx.font = `${fontScale}px ${fontFamily}`;
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle'; 
        ctx.fillStyle = '#000';
        ctx.fillText(text.toString(), 0, 0); 
        ctx.restore(); 
    }
    drawText("y", x + (width * 0.5), y - off1 - txtOff1, fontSize, 0);
    drawText("x", x + width + off1 + txtOff1, y + (height * 0.5), fontSize, 0);
})(); 