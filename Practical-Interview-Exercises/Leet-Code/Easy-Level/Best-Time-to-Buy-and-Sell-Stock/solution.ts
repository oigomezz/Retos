function maxProfit(prices: number[]): number {
  let minPrice = Infinity;
  let maxProfit = 0;

  for (const element of prices) {
    if (element < minPrice) minPrice = element;
    else if (element - minPrice > maxProfit) maxProfit = element - minPrice;
  }

  return maxProfit;
}
