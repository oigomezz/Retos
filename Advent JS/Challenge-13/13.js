function calculateTime(deliveries) {
  const H = 60*60;
  const M = 60;
  let time = -7*H;
  for (const delivery of deliveries) {
    const [h,m,s] = delivery.split(':').map(Number);
    time += h*H + m*M + s;
  }

  const sign = '-'.repeat(time < 0);
  time = Math.abs(time);
  const hh = Math.floor(time / H).toString().padStart(2, '0');
  time %= H;
  const mm = Math.floor(time/ M).toString().padStart(2, '0');
  time %= M;
  const ss = time.toString().padStart(2, '0');
  return `${sign}${hh}:${mm}:${ss}`;
}

console.log(calculateTime(["00:10:00", "01:00:00", "03:30:00"])); // '-02:20:00'
console.log(calculateTime(["02:00:00", "05:00:00", "00:30:00"])); // '00:30:00'
console.log(calculateTime(["00:45:00", "00:45:00", "00:00:30", "00:00:30"])); // '-05:29:00'