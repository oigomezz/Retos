function perfectNumber(num) {
  if (num <= 1) return false;
  let divisors = 0;
  for (let i = 1; i < num; i++) if (num % i === 0) divisors += i;
  return divisors === num;
}
