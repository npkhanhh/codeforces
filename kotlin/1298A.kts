fun main(args: Array<String>) {
    val a = readLine()!!.split(' ').map { it.toInt() }.toIntArray()
    a.sort()
    var b = (0 until 3).map { a[3] - a[it] }.toTypedArray()
    println(b.joinToString(separator = " "))
}