const API_DATE_REGEX = /^(\d{2})-(\d{2})-(\d{4})$/

export function isValidApiDate(value: string): boolean {
  const match = API_DATE_REGEX.exec(value)
  if (!match) {
    return false
  }

  const [, day, month, year] = match
  const parsedDate = new Date(Number(year), Number(month) - 1, Number(day))

  return (
    parsedDate.getFullYear() === Number(year) &&
    parsedDate.getMonth() === Number(month) - 1 &&
    parsedDate.getDate() === Number(day)
  )
}

export function formatInputDateToApi(value: string): string {
  if (!value) {
    return ''
  }

  const [year, month, day] = value.split('-')

  return `${day}-${month}-${year}`
}

export function formatApiDateToInput(value: string): string {
  const match = API_DATE_REGEX.exec(value)
  if (!match) {
    return ''
  }

  const [, day, month, year] = match

  return `${year}-${month}-${day}`
}
