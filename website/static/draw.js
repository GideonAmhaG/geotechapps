const canvas = document.getElementById("myCanvas");
const ctx = canvas.getContext("2d");
canvas.width = 1000;
canvas.height = 2000;
const b = parseFloat(document.getElementById('b-value').value);
const d = parseFloat(document.getElementById('d-value').value);
const N = parseFloat(document.getElementById('N-value').value);
const s = parseFloat(document.getElementById('s-value').value);
const bar = parseFloat(document.getElementById('bar-value').value);
const col = parseFloat(document.getElementById('col-value').value);
const coly = parseFloat(document.getElementById('col-valuey').value);
const cov = parseFloat(document.getElementById('cov-value').value);
const xCor = 100;
const yCor = 15;
const topCov = 75;
const cur = Math.ceil((d - ((cov + topCov) * 0.001)) * 100) / 100;
const barXLen = b - (2 * topCov * 0.001);
const mul = 100;
const x = mul * b
const y1 = mul * b
const y2 = mul * d
const xCol = mul * col;
const yCol = mul * coly;
const curScaled = mul * cur;
const horzSpace = 30 + (x * 0.4);
const vertSpace = 50 + (y1 * 0.7);
const xScale = 0.75;
const y1Scale = 0.75;
const vsScale = 0.2;
const vsScaleBar = 0.6;
const dimWidth = 20;
const offset1 = 5;
const offset2 = 20;
const offset3 = 20;
const offset5 = 4;
const colHeight = y1 * 0.23;
const dotRadius = mul * 0.03;
const offSet7 = 4;
const barOff = 4;
ctx.strokeStyle = "black";
ctx.lineWidth = 1.3;
// plan view
ctx.rect(xCor, yCor, x, y1);
ctx.fillStyle = "#999999";
ctx.fillRect(xCor + (x * 0.5) - (xCol * 0.5), yCor + (y1 * 0.5) - (yCol * 0.5), xCol, yCol);
ctx.stroke();
// section view
// footing
ctx.beginPath();
ctx.moveTo(xCor + (x * 0.5) - (xCol * 0.5), yCor + y1 + vertSpace);
ctx.lineTo(xCor + (x * 0.5) - (xCol * 0.5), yCor + y1 + vertSpace + colHeight);
ctx.lineTo(xCor, yCor + y1 + vertSpace + colHeight);
ctx.lineTo(xCor, yCor + y1 + vertSpace + colHeight + y2);
ctx.lineTo(xCor + x, yCor + y1 + vertSpace + colHeight + y2);
ctx.lineTo(xCor + x, yCor + y1 + vertSpace + colHeight);
ctx.lineTo(xCor + (x * 0.5) + (xCol * 0.5), yCor + y1 + vertSpace + colHeight);
ctx.lineTo(xCor + (x * 0.5) + (xCol * 0.5), yCor + y1 + vertSpace);
// col bar
const colBarOff = 4;
const cOBot = 1.5;
ctx.moveTo(xCor + (x * 0.5) - (xCol * 0.5) + colBarOff, yCor + y1 + vertSpace);
ctx.lineTo(xCor + (x * 0.5) - (xCol * 0.5) + colBarOff, yCor + y1 + vertSpace + colHeight + y2 - barOff - offSet7 - dotRadius - cOBot);
ctx.lineTo(xCor + (x * 0.5) - (xCol * 0.5) + colBarOff - curScaled, yCor + y1 + vertSpace + colHeight + y2 - barOff - offSet7 - dotRadius - cOBot);
ctx.moveTo(xCor + (x * 0.5) + (xCol * 0.5) - colBarOff, yCor + y1 + vertSpace);
ctx.lineTo(xCor + (x * 0.5) + (xCol * 0.5) - colBarOff, yCor + y1 + vertSpace + colHeight + y2 - barOff - offSet7 - dotRadius - cOBot);
ctx.lineTo(xCor + (x * 0.5) + (xCol * 0.5) - colBarOff + curScaled, yCor + y1 + vertSpace + colHeight + y2 - barOff - offSet7 - dotRadius - cOBot);
const numLns = Math.floor(b) + 2; 
const lineLen = (xCor + (x * 0.5) + (xCol * 0.5) - colBarOff) - (xCor + (x * 0.5) - (xCol * 0.5) + colBarOff);
const vertSpacBars = 15; 
const xBSrt = xCor + (x * 0.5) - (xCol * 0.5) + colBarOff; 
const yBSrt = yCor + y1 + vertSpace + 5; 
for (let i = 0; i < numLns; i++)
{
    const yPosition = yBSrt + i * (vertSpacBars);
    ctx.moveTo(xBSrt, yPosition);
    ctx.lineTo(xBSrt + lineLen, yPosition);
}
// plan view bar and centerline                                                 
// vert rebar
ctx.moveTo(xCor + (x * xScale) - curScaled, yCor + offset1);
ctx.lineTo(xCor + (x * xScale), yCor + offset1);
ctx.lineTo(xCor + (x * xScale), yCor + y1 - offset1);
ctx.lineTo(xCor + (x * xScale) - curScaled, yCor + y1 - offset1);
ctx.moveTo(xCor + x + horzSpace - curScaled, yCor + offset1);
ctx.lineTo(xCor + x + horzSpace, yCor + offset1);
ctx.lineTo(xCor + x + horzSpace, yCor + y1 - offset1);
ctx.lineTo(xCor + x + horzSpace - curScaled, yCor + y1 - offset1);
// horz rebar
ctx.moveTo(xCor + offset1, yCor + (y1 * y1Scale) - curScaled);
ctx.lineTo(xCor + offset1, yCor + (y1 * y1Scale));
ctx.lineTo(xCor + x - offset1, yCor + (y1 * y1Scale));
ctx.lineTo(xCor + x - offset1, yCor + (y1 * y1Scale) - curScaled);
ctx.moveTo(xCor + offset1, yCor + y1 + (vertSpace * vsScaleBar) - curScaled);
ctx.lineTo(xCor + offset1, yCor + y1 + (vertSpace * vsScaleBar));
ctx.lineTo(xCor + x - offset1, yCor + y1 + (vertSpace * vsScaleBar));
ctx.lineTo(xCor + x - offset1, yCor + y1 + (vertSpace * vsScaleBar) - curScaled);
// section view bar
ctx.moveTo(xCor + offset1, yCor + y1 + vertSpace + colHeight + y2 - barOff - curScaled);
ctx.lineTo(xCor + offset1, yCor + y1 + vertSpace + colHeight + y2 - barOff);
ctx.lineTo(xCor + x - offset1, yCor + y1 + vertSpace + colHeight + y2 - barOff);  
ctx.lineTo(xCor + x - offset1, yCor + y1 + vertSpace + colHeight + y2 - barOff - curScaled);  
ctx.stroke();
// centerline plan view and col top
ctx.beginPath();
const cenLineOff = 15;
ctx.moveTo(xCor + (x * 0.5), yCor - cenLineOff);
ctx.lineTo(xCor + (x * 0.5), yCor + y1 + cenLineOff);
ctx.moveTo(xCor - cenLineOff, yCor + (y1 * 0.5));
ctx.lineTo(xCor + x + cenLineOff, yCor + (y1 * 0.5));
ctx.moveTo(xCor + (x * 0.5) - (xCol * 0.5) + colBarOff - 20, yCor + y1 + vertSpace);
ctx.lineTo(xCor + (x * 0.5) + (xCol * 0.5) - colBarOff + 20, yCor + y1 + vertSpace);
ctx.lineWidth = 0.5;
ctx.stroke();
const numDots = N;
const xCStart = xCor + offset1 + 4; 
const xCEnd = xCor + x - offset1 - 4; 
const width = xCEnd - xCStart - dotRadius * 2 + offset5;
const yC = yCor + y1 + vertSpace + colHeight + y2 - barOff - offSet7;
const spacing = width / (numDots - 1); 
for (let i = 0; i < numDots; i++)
{
    let x = xCStart + (spacing * i); 
    if (i === numDots - 1) x = xCEnd;
    ctx.beginPath();
    ctx.arc(x, yC, dotRadius, 0, 2 * Math.PI);
    ctx.fillStyle = "black";
    ctx.fill();
    ctx.closePath();
}
// arrows
const arrOff1 = 35;
const arrOff2 = 8;
const arrOff3 = 15 * x * 0.009;
const data =
[
    { startX: xCor + x + arrOff1, startY: yCor, endX: xCor + x + arrOff1, endY: yCor + y1 },
    { startX: xCor, startY: yCor + y1 + arrOff1, endX: x + xCor, endY:  yCor + y1 + arrOff1},
    { startX: xCor + x + arrOff2, startY: yCor + y1 + vertSpace + colHeight + y2, endX: xCor + x + arrOff2, endY: yCor + y1 + vertSpace + colHeight },
    { startX: xCor + x + arrOff2, startY: yCor, endX: xCor + x + arrOff2, endY: yCor + (y1 * 0.5) },
    { startX: xCor + x + arrOff2, startY: yCor + (y1 * 0.5), endX: xCor + x + arrOff2, endY: yCor + y1 },
    { startX: xCor, startY: yCor + y1 + arrOff2, endX: xCor + (x * 0.5), endY: yCor + y1 + arrOff2 },
    { startX: xCor + (x * 0.5), startY: yCor + y1 + arrOff2, endX: xCor + x, endY: yCor + y1 + arrOff2 },
    { startX: xCor, startY: yCor + y1 + vertSpace + arrOff3, endX: xCor + (x * 0.5) - (xCol * 0.5), endY: yCor + y1 + vertSpace + arrOff3 },
    { startX: xCor + (x * 0.5) - (xCol * 0.5), startY: yCor + y1 + vertSpace - arrOff2, endX: xCor + (x * 0.5) + (xCol * 0.5), endY: yCor + y1 + vertSpace - arrOff2 },
    { startX: xCor + (x * 0.5) + (xCol * 0.5), startY: yCor + y1 + vertSpace + arrOff3, endX: xCor + x, endY: yCor + y1 + vertSpace + arrOff3 },
];
const lineWidth = 0.9;
const arrowHeadSize = 5.5;
const fontSize = 12;
const fontFamily = 'Arial';
const textColor = 'black';
function drawArrowhead(ctx, startX, startY, endX, endY, size)
{
    const angle = Math.atan2(endY - startY, endX - startX);
    const headLength = size * 4; 
    const headWidth = size * 4; 
    const arrowX1 = endX - headLength * Math.cos(angle + Math.PI / 3);
    const arrowY1 = endY - headLength * Math.sin(angle + Math.PI / 3);
    const arrowX2 = endX - headLength * Math.cos(angle - Math.PI / 3);
    const arrowY2 = endY - headLength * Math.sin(angle - Math.PI / 3);
    const offsetX1 = headWidth * Math.cos(angle + Math.PI / 2);
    const offsetY1 = headWidth * Math.sin(angle + Math.PI / 2);
    const offsetX2 = headWidth * Math.cos(angle - Math.PI / 2);
    const offsetY2 = headWidth * Math.sin(angle - Math.PI / 2);
    ctx.beginPath();
    ctx.moveTo(endX, endY);
    ctx.lineTo(arrowX1 + offsetX1, arrowY1 + offsetY1);
    ctx.lineTo(arrowX2 + offsetX2, arrowY2 + offsetY2);
    ctx.closePath();
    ctx.fillStyle = 'black';
    ctx.fill();
}
function drawDimensionLine(ctx, lineData)
{
    const { startX, startY, endX, endY } = lineData;
    ctx.beginPath();
    ctx.moveTo(startX, startY);
    ctx.lineTo(endX, endY);
    ctx.lineWidth = lineWidth;
    ctx.strokeStyle = 'black';
    ctx.stroke();
    drawArrowhead(ctx, startX, startY, endX, endY, arrowHeadSize);
    drawArrowhead(ctx, endX, endY, startX, startY, arrowHeadSize);
}
for (const lineData of data)
{
    drawDimensionLine(ctx, lineData);
}
// text
const scaleFont = 1.4;
var barFontScale = 1.4;
var offset4 = 40;
if (b < 2.3)
{
    barFontScale = barFontScale < (x * 0.01) ? barFontScale : (x * 0.01);
    offset4 = x * 0.27;
} 
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
const txtOff1 = 20;
const txtOff2 = 48;
const txtOff3 = 8;
const txtOff4 = 12;
const txtOff5 = 20;
drawText(d * 1000, xCor + x + txtOff1, yCor + y1 + vertSpace + colHeight + (y2 * 0.5), fontSize * scaleFont, 270 );
drawText(b * 1000, xCor + x + txtOff2, yCor + (y1 * 0.5), fontSize * scaleFont, 270 );
drawText(b * 500, xCor + x + txtOff1, yCor + (y1 * 0.25), fontSize * scaleFont, 270 );
drawText(b * 500, xCor + x + txtOff1, yCor + (y1 * 0.75), fontSize * scaleFont, 270 );
drawText(b * 1000, xCor + (x * 0.5), yCor + y1 + txtOff2, fontSize * scaleFont, 0 );
drawText(b * 500, xCor + (x * 0.25), yCor + y1 + txtOff1, fontSize * scaleFont, 0 );
drawText(b * 500, xCor + (x * 0.75), yCor + y1 + txtOff1, fontSize * scaleFont, 0 );
drawText(Math.round(((b * 0.5) - (col * 0.5)) * 1000), xCor + (x * 0.21), yCor + y1 + vertSpace + arrOff3 - txtOff3, fontSize * scaleFont, 0 );
drawText(Math.round(((b * 0.5) - (col * 0.5)) * 1000), xCor + (x * 0.79), yCor + y1 + vertSpace + arrOff3 - txtOff3, fontSize * scaleFont, 0 );
drawText(Math.round(col * 1000), xCor + (x * 0.5), yCor + y1 + vertSpace - arrOff2 - txtOff4, fontSize * scaleFont, 0 );
drawText(N + "ϕ" + bar + "@" + s + "-" + Math.round(((2 * cur) + barXLen) * 1000), xCor + (x * 0.5), yCor + y1 + (vertSpace * vsScaleBar) - txtOff4, fontSize * barFontScale, 0);
drawText(Math.round(barXLen * 1000), xCor + (x * 0.5), yCor + y1 + (vertSpace * vsScaleBar) + txtOff4, fontSize * barFontScale, 0);
drawText(Math.round(cur * 1000), xCor - txtOff3, yCor + y1 + (vertSpace * vsScaleBar) - (curScaled * 0.5), fontSize * barFontScale, 270);
drawText(Math.round(cur * 1000), xCor + x + txtOff3, yCor + y1 + (vertSpace * vsScaleBar) - (curScaled * 0.5), fontSize * barFontScale, 270);
drawText(N + "ϕ" + bar + "@" + s + "-" + Math.round(((2 * cur) + barXLen) * 1000), xCor + x + horzSpace - txtOff4, yCor + (y1 * 0.5), fontSize * barFontScale, 270);
drawText(Math.round(barXLen * 1000), xCor + x + horzSpace + txtOff4, yCor + (y1 * 0.5), fontSize * barFontScale, 270);
drawText(Math.round(cur * 1000), xCor + x + horzSpace - (curScaled * 0.5), yCor - txtOff3, fontSize * barFontScale, 0);
drawText(Math.round(cur * 1000), xCor + x + horzSpace - (curScaled * 0.5), yCor + y1 + txtOff3, fontSize * barFontScale, 0);
drawText("A", xCor - txtOff5, yCor + (y1 * 0.5), fontSize * scaleFont, 0);
drawText("A", xCor + x + txtOff5, yCor + (y1 * 0.5), fontSize * scaleFont, 0);
drawText("Section A-A", xCor + (x * 0.5), yCor + y1 + vertSpace + colHeight + y2 + txtOff1, fontSize * scaleFont, 0);